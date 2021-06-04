function generate_json_in_state(data){
    // Segun el catalogo la propiedad RESULTADO nos indica si dio positivo a covid y se tomara como fecha 
    // "FECHA_SINTOMAS" a su vez se filtrará por la entidad ENTIDAD_RES para Sonora donde su ID es 26,
    // esto lo estare agregndo a un arreglo para despues imprimirlo en pantalla y generar el .csv
    pac_son_covid = [];
    var count_covid = 0;
    for(let i = 0; i < data.length; i++){
        if(data[i].ENTIDAD_RES == 26 && data[i].RESULTADO == 1){
            // Voy a contar cuantos usuarios quedaron dentro del arrego
            count_covid++;
            // Agrego la etique de hombre o mujer para que se diferecie mejor
            let gender;
            if(data[i].SEXO == 1){
                gender = "Mujer";
            }else{
                gender = "Hombre";
            }

            // Valido si murio o no el infectado para que se pueda ver en la tabla correctamente
            let demise;
            let demise_date;
            if(data[i].FECHA_DEF != "9999-99-99"){
                demise = "Fallecido";
                demise_date = data[i].FECHA_DEF;
            }else{
                demise = "Vive"
                data[i].FECHA_DEF
                demise_date = "N/A"
            }

            // Genero un arreglo de objetos para despues imprimirlos en la tabla
            pac_son_covid[i]={
                date: data[i].FECHA_SINTOMAS,
                register_id: data[i].ID_REGISTRO,
                gender: gender,
                demise: demise,
                demise_date: demise_date
            }
        }

    }

    // Aqui le doy formato al arreglo para que genere el CSV correctamente y lo mando a la funcion
    // para que se descargue automaticamente
    example = [
        ['id','date','demise','demise_date','gender']
    ];
    pac_son_covid.forEach((pac)=>{
        example2 =[];
        example2.push(pac.register_id);
        example2.push(pac.date);
        example2.push(pac.demise);
        example2.push(pac.demise_date);
        example2.push(pac.gender);
        example.push(example2)
    });
    exportToCsv("tabla1.csv",example);

    loadTableData(pac_son_covid)
}

function loadTableData(items) {
    // Agero la informacion a la tabla indicandole la columna y el registro que se agregara
    const table = document.getElementById("testBody");
    items.forEach( item => {
      let row = table.insertRow();
  
      let id = row.insertCell(0);
      id.innerHTML = item.register_id;

      let date = row.insertCell(1);
      date.innerHTML = item.date;

      let demise = row.insertCell(2);
      demise.innerHTML = item.demise;

      let demise_date = row.insertCell(3);
      demise_date.innerHTML = item.demise_date;

      let gender = row.insertCell(4);
      gender.innerHTML = item.gender;

    });
  }