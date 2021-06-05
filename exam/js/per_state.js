function cant_pac_per_state(data){
    //INICIANDO CONTADORES
    let sr = 0; //SONORA id = 26
    let ch = 0; //CHIHUAHUA id = 08
    let nl = 0; //NUEVO LEON id = 19
    let pl = 0; //PUEBLA id = 21

    for(let i = 0; i < data.length; i++){
        if(data[i].ENTIDAD_RES == 26 && data[i].RESULTADO == 1){
            sr++;

        }else if(data[i].ENTIDAD_RES == 08 && data[i].RESULTADO == 1){
            ch++;
        }
        else if(data[i].ENTIDAD_RES == 19 && data[i].RESULTADO == 1){
            nl++;
        }
        else if(data[i].ENTIDAD_RES == 21 && data[i].RESULTADO == 1){
            pl++;
        }
    }

    count_state=[
                    {
                        state:"Sonora",
                        total: sr
                    },
                    {
                        state:"Chihuahua",
                        total: ch
                    },
                    {
                        state:"Nuevo León",
                        total: nl
                    },
                    {
                        state:"Puebla",
                        total: pl
                    }
                ]

    // Manda llamar la funcion que genera el csv, ya formateado para que se imprima correctamente
    headers = [
        ['state','qty']
    ];
    count_state.forEach((st)=>{
        to_push =[];
        to_push.push(st.state);
        to_push.push(st.total);
        headers.push(to_push)
    });
    exportToCsv("tabla2.csv",headers);

    // Se manda llamar la funcion para pintar la segunda tabla en la tab 2
    load_table_per_state(count_state);

    // Llama la funcion que grafica la informacion en la otra tab
    states=['Sonora','Chihuahua','Nuevo Leon','Puebla']
    data_cont=[sr,ch,nl,pl];
    graph(states,data_cont);
}


function load_table_per_state(items) {
    // Agrego la informacion a la tabla indicandole la columna y el registro que se agregara
    const table = document.getElementById("count_states");
    items.forEach( item => {
      let row = table.insertRow();
  
      let name = row.insertCell(0);
      name.innerHTML = item.state;

      let state = row.insertCell(1);
      state.innerHTML = item.total;

    });
  }

function graph(labels,info){
    var densityData = {
        label: 'Total',
        data: info,
        backgroundColor: [
            'rgba(0, 99, 132, 0.6)',
            'rgba(30, 99, 132, 0.6)',
            'rgba(60, 99, 132, 0.6)',
            'rgba(90, 99, 132, 0.6)'
        ]
      };

    var atx = document.getElementById("myChart").getContext("2d");
    const barChart = new Chart(atx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [densityData]
        }
    });
}