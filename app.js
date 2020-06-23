
var data = [];

//Evento que procesa carga archivo CSV y guarda en datos en variabla global data
$("#archivo").change(function(e){

    data = [];
    var ext = $("#archivo").val().split(".").pop().toLowerCase();
    if($.inArray(ext, ["csv"]) == -1) {
        alert('archivo no es CSV');
        return false;
    } 

    if (e.target.files != undefined) {
        var reader = new FileReader();
        reader.onload = function(e) {
            var lines = e.target.result.split('\r\n');
            for (i = 1; i < lines.length - 1; ++i)
            {
                var splitedData = lines[i].split(",").map((item) => {
                    item = item.replace(/"/g, ""); //quitar comillas
                    return item;
                });

                var tempData = {
                    "FECHA_ACTUALIZACION": splitedData[0],
                    "ID_REGISTRO": splitedData[1],
                    "ORIGEN": splitedData[2],
                    "SECTOR": splitedData[3],
                    "ENTIDAD_UM": splitedData[4],
                    "SEXO": splitedData[5],
                    "ENTIDAD_NAC": splitedData[6],
                    "ENTIDAD_RES": splitedData[7],
                    "MUNICIPIO_RES": splitedData[8],
                    "TIPO_PACIENTE": splitedData[9],
                    "FECHA_INGRESO": splitedData[10],
                    "FECHA_SINTOMAS": splitedData[11],
                    "FECHA_DEF": splitedData[12],
                    "INTUBADO": splitedData[13],
                    "NEUMONIA": splitedData[14],
                    "EDAD": splitedData[15],
                    "NACIONALIDAD": splitedData[16],
                    "EMBARAZO": splitedData[17],
                    "HABLA_LENGUA_INDIG": splitedData[18],
                    "DIABETES": splitedData[19],
                    "EPOC": splitedData[20],
                    "ASMA": splitedData[21],
                    "INMUSUPR": splitedData[22],
                    "HIPERTENSION": splitedData[23],
                    "OTRA_COM": splitedData[24],
                    "CARDIOVASCULAR": splitedData[25],
                    "OBESIDAD": splitedData[26],
                    "RENAL_CRONICA": splitedData[27],
                    "TABAQUISMO": splitedData[28],
                    "OTRO_CASO": splitedData[29],
                    "RESULTADO": splitedData[30],
                    "MIGRANTE": splitedData[31],
                    "PAIS_NACIONALIDAD": splitedData[32],
                    "PAIS_ORIGEN": splitedData[33],
                    "UCI": splitedData[34]
                }
                data.push(tempData);
            }
            $("#res").append("Archivo cargado.\n");
            var pro = $("#pro").val();
            if(pro == 1)
                processData(); //tabla 1
            else if(pro == 2)
                processDataHospitalizados(); //tabla 2 y grafica 1
            else if (pro == 3)
                processDataNationalConfirmed(); //grafica 2

        };
        $("#res").append("Cargando archivo...\n");
        reader.readAsText(e.target.files.item(0));
    }
    return false;

});

//Procesa datos nacionales y genera gráfica 2
function processDataNationalConfirmed(){

    //Obtener registros de casos confirmados, resultado prueba == 1
    var confirmedCases = data.filter((item) => item.RESULTADO == "1");
    
    //Fechas únicas, basadas en fecha de ingreso
    var ingressDates = data.map((item) => item.FECHA_INGRESO);
    var uniqueDates = ingressDates.reduce((unique, item) => {
        return unique.includes(item) ? unique : [...unique, item];
    }, []); //quitamos duplicados

    //Por cada fecha, calcular el número de casos confirmados de ese día
    var resData = [];
    $.each(uniqueDates, function(){

        var currentDate = this;
        var confirmedCasesOfDay = confirmedCases.filter((item) => item.FECHA_INGRESO == currentDate);

        resData.push({ date : currentDate, confirmedCases : confirmedCasesOfDay.length });

    });

    //Ordernar datos por fecha y graficar
    drawChart2(resData.sort((a,b) => {
        return new Date(a.date) - new Date(b.date);
    }) );


}


//Procesar tabla 2: hospitalizados de Sonora, Chihuahua, Nuevo León y Puebla.
function processDataHospitalizados()
{
    $("#res").append(`Procesando datos ${data.length} para estados hospitalizados..\n`);

    //Obtener registros de los estados son, chihuahua, neuvo leon y puebla
    var estadosData = data.filter((item) => {
        return item.ENTIDAD_RES == "26" || //son
        item.ENTIDAD_RES == "08" || //chi
        item.ENTIDAD_RES == "19"|| //nuevo leon
        item.ENTIDAD_RES == "21"; //pruebla
    });

    $("#res").append(`Datos de Sonora, Chihuahua, Nuevo León, Puebla encontrados ${estadosData.length}\n`);

    //Filtrar hospitalizados por ese estado
    var hospitalizedData = estadosData.filter((item) => item.TIPO_PACIENTE == "2" );
    $("#res").append(`Hospitalizados en Sonora, Chihuahua, Nuevo León, Puebla encontrados ${hospitalizedData.length}\n`);

    var resData = [{
        state : "Sonora", id : "26", hospitalized : 0
    },
    {
        state : "Chihuahua", id : "08", hospitalized : 0
    },
    {
        state : "Nuevo León", id : "19", hospitalized : 0
    },
    {
        state : "Puebla", id : "21", hospitalized : 0
    }];  

        
    //Por cada estado, calcular los hospitalizados
    $.each(resData, function(){
        var state = this;
        this.hospitalized = hospitalizedData.filter((item) => item.ENTIDAD_RES == state.id).length;
    })

    //Graficar
    drawTable2(resData, resData.length);

}


//Procesar tabla1 : casos de Sonora -> fecha, confirmados, y decesos
function processData(){
    
    $("#res").append(`Procesando datos ${data.length} para Sonora...\n`);
   
    //ID_REGISTRO CASO
    //TIPO_PACIENTE: AMBULATORIO si regreso, HOSPITALIZADO se quedo en hospital
    //FECHA_SINTOMAS FECHA INICIO SINTOMAS
    //RESULTADO RESULTADO DE PRUEBA
    //FECA_DEF fecha defuncion

    //(a) Fecha
    //(b) Confirmados de SARS-CoV2 en Sonora por fecha usando la fecha de inicio de síntomas (no acumulados)
    //(c) Decesos (entre los confirmados) por fecha.

    //Obtener registros de sonora
    var sonoraData = data.filter((item) => {
        return item.ENTIDAD_RES == "26"; //sonora
    });

    $("#res").append(`Datos de Sonora encontrado ${sonoraData.length}\n`);

    //obtener fechas de casos de sonora en base a la fecha de sintomas y quitar duplicados
    var sympthomsDates = data.map((item) => item.FECHA_SINTOMAS);
    var uniqueDates = sympthomsDates.reduce((unique, item) => {
        return unique.includes(item) ? unique : [...unique, item];
    }, []);

    $("#res").append(`Fechas unicas ${uniqueDates.length}\n`);

    //calcular por dia el numero casos confirmados y fallecimientos
    var resData = [];
    $.each(uniqueDates, function(){
        var tempDate = this;

        var dateCases = sonoraData.filter((item) => item.FECHA_SINTOMAS == tempDate );
        //calcular numero de casos confirmados a partir de la fecha de sintomas
        var confirmedCases = dateCases.filter((item) => item.RESULTADO == "1");
        //calcular numero de fallecimientos confirmados cuya fecha de fallecimiento es hoy
        var deathCases = sonoraData.filter((item) => item.RESULTADO == "1" && item.FECHA_DEF== tempDate );

        resData.push({ 
            date : tempDate, 
            confirmedCases : confirmedCases.length,
            deathCases : deathCases.length
        });

    });

    //Generar tabla
    drawTable(resData.sort((a,b) => {
        return new Date(a.date) - new Date(b.date);
    }), resData.length);

}

//Genera tabla preview en html y genera archivo CSV: Sonora
function drawTable(resData, limit = 10000){

    if(limit > resData.length)
        limit = resData.length;

    $("#res").append(`Generando tabla con primeros ${limit} resultados\n`);

    $("#tbSonora").html("");
    var tempHtml = "<thead><tr><th>date</th><th>confirmed</th><th>deaths</th></tr></thead><tbody>";
    if(resData.length > 0){
        for(var i = 0; i < limit; i++){
            tempHtml+= `<tr><td>${resData[i].date}</td><td>${resData[i].confirmedCases}</td><td>${resData[i].deathCases}</td></tr>`
        }
    }
    tempHtml+= "</tbody>";
    $("#tbSonora").html(tempHtml);

    genereteCSVFile(resData);
}

//Genera tabla preview en html y genera archivo CSV  y gráfica 1 - Son, Chi, Nuevo Leon, Puebla
function drawTable2(resData, limit = 10000){

    if(limit > resData.length)
        limit = resData.length;

    $("#res").append(`Generando tabla con primeros ${limit} resultados\n`);

    $("#tbSonora").html("");
    var tempHtml = "<thead><tr><th>estado</th><th>id</th><th>hospitalizados</th></tr></thead><tbody>";
    if(resData.length > 0){
        for(var i = 0; i < limit; i++){
            tempHtml+= `<tr><td>${resData[i].state}</td><td>${resData[i].id}</td><td>${resData[i].hospitalized}</td></tr>`
        }
    }
    tempHtml+= "</tbody>";
    $("#tbSonora").html(tempHtml);

    genereteCSVFile(resData);

    drawChart1(resData);

}

//Convierte objeto json en string compatible CSV
function ConvertToCSV(objArray) {
    var array = typeof objArray != 'object' ? JSON.parse(objArray) : objArray;
    var str = '';
    for (var i = 0; i < array.length; i++) {
        if(i == 0)
        {
            //headers
            var pro = $("#pro").val();
            if(pro == 1)
                str += "fecha,confirmados,decesos" + '\r\n';
            else if(pro == 2)
                str += "estado,id,hospitalizados" + '\r\n';
        }
        var line = '';
        for (var index in array[i]) {
            if (line != '') line += ','
            line += array[i][index];
        }
        str += line + '\r\n';
    }
    return str;
}

//genera archivo CSV para descargar por medio de liga, 
function genereteCSVFile(data){
 
    var text = ConvertToCSV(data);
    var type = "text/csv";

    var dlbtn = document.getElementById("btnDownload");
    var file = new Blob([text], {type: type});
    dlbtn.href = URL.createObjectURL(file);
    dlbtn.download = name;
}

//Gráfica serie tiempo confirmados a nivel nacional 
function drawChart2(data){

    var series = data.map((item) => item.confirmedCases );
    var categories = data.map((item) => item.date );
    var convertedData = [{ name : "Casos confirmados", data : series }];

    Highcharts.chart('grafica', {
        title: {
            text: 'Gráfica 2'
        },
        yAxis: {
            title: {
                text: 'Casos confirmados'
            }
        },
        xAxis: {
            categories:  categories
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle'
        },
        series: convertedData 
    });

}

//Gráfica acumulados de hospitalizados por estado
function drawChart1(data){

    var convertedData = data.map((item) => { return { name : item.state, data : [item.hospitalized] } });

    Highcharts.chart('grafica', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Gráfica 1'
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Hospitalizados (casos)'
            }
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: convertedData 
    });

}