function create_graph2(data){
    date = [];
    date_count = [];

    // Se inicializa en 0 los contadores para sacar los del mes
      let jan = 0;
      let feb = 0;
      let mar = 0;
      let apr = 0;
      let may = 0;

    // Se recorre el arreglo para sacar la cantidad por mes y poder graficarlo
      for(let j = 0; j < data.length; j++){
        if(data[j].FECHA_INGRESO == null){
        }else{
            let month = data[j].FECHA_INGRESO.slice(5,7);
            if(month == "01"){
                jan++;
            } else if (month == "02"){
                feb++;
            }
            else if (month == "03"){
                mar++;
            }
            else if (month == "04"){
                apr++;
            }
            else if (month == "05"){
                may++;
            }else{
                console.log("No hace nada");
            }
        }
    }

    // Se envian los nombres y la informacion a graficar
    months=["Enero", "Febrero", "Marzo", "Abril", "Mayo"]
    data_cont=[jan,feb,mar,apr,may];
    graph2(months,data_cont);
  }


  function graph2(labels,info){
    var speedData = {
        labels: labels,
        datasets: [{
          label: "Totales por mes",
          data: info,
        }]
      };
       
      var chartOptions = {
        legend: {
          display: true,
          position: 'top',
          labels: {
            boxWidth: 80,
            fontColor: 'black'
          }
        }
      };

      var lineChart = new Chart(myChart2, {
        type: 'line',
        data: speedData,
        options: chartOptions
    });
}