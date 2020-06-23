
var data = [];

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
                    //quitar comillas
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
            //processData(); //tabla 1
            processDataHospitalizados(); //tabla 2
        };
        $("#res").append("Cargando archivo...\n");
        reader.readAsText(e.target.files.item(0));
    }
    return false;

});



//Procesar tabla 2: hospitalizados de Sonora, Chihuahua, Nuevo León y Puebla.
function processDataHospitalizados()
{
    $("#res").append(`Procesando datos ${data.length} para estados hospitalizados..\n`);

    var estadosData = data.filter((item) => {
        return item.ENTIDAD_RES == "26" || //son
        item.ENTIDAD_RES == "08" || //chi
        item.ENTIDAD_RES == "19"|| //nuevo leon
        item.ENTIDAD_RES == "21"; //pruebla
    });

    $("#res").append(`Datos de Sonora, Chihuahua, Nuevo León, Puebla encontrados ${estadosData.length}\n`);

    debugger;
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

        

    $.each(resData, function(){
        var state = this;
        this.hospitalized = hospitalizedData.filter((item) => item.ENTIDAD_RES == state.id).length;
    })

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

    var sonoraData = data.filter((item) => {
        return item.ENTIDAD_RES == "26"; //sonora
    });

    $("#res").append(`Datos de Sonora encontrado ${sonoraData.length}\n`);

    //var uniqueDates = $.unique(data.map((item) => item.FECHA_SINTOMAS));
    //var uniqueDates = $.unique(sonoraData.map((item) => item.FECHA_SINTOMAS));

    var sympthomsDates = data.map((item) => item.FECHA_SINTOMAS);
    var uniqueDates = sympthomsDates.reduce((unique, item) => {
        return unique.includes(item) ? unique : [...unique, item];
    }, []);
    debugger;

    $("#res").append(`Fechas unicas ${uniqueDates.length}\n`);

    var resData = [];
    $.each(uniqueDates, function(){
        var tempDate = this;

        
        var dateCases = sonoraData.filter((item) => item.FECHA_SINTOMAS == tempDate );

        var confirmedCases = dateCases.filter((item) => item.RESULTADO == "1");
        //var deathCases = confirmedCases.filter((item) => item.FECA_DEF == tempDate); 
        var deathCases = sonoraData.filter((item) => item.RESULTADO == "1" && item.FECHA_DEF== tempDate );

        resData.push({ 
            date : tempDate, 
            confirmedCases : confirmedCases.length,
            deathCases : deathCases.length
        });

    });

    drawTable(resData.sort((a,b) => {
        return new Date(a.date) - new Date(b.date);
    }), resData.length);

}

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
}

function ConvertToCSV(objArray) {
    var array = typeof objArray != 'object' ? JSON.parse(objArray) : objArray;
    var str = '';
    for (var i = 0; i < array.length; i++) {
        if(i == 0)
        {
            //headers
            //str += "fecha,confirmados,decesos" + '\r\n';
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

function genereteCSVFile(data){
 
    var text = ConvertToCSV(data);
    var type = "text/csv";

    var dlbtn = document.getElementById("btnDownload");
    var file = new Blob([text], {type: type});
    dlbtn.href = URL.createObjectURL(file);
    dlbtn.download = name;
}