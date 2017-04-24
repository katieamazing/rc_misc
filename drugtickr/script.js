data = {
  'MJ': [20, 22, 18, 20],
  'H' : [65, 86, 65, 62],
  'CRCK' : [34, 33, 39, 40]
}

function makeyTable(data) {
  var table = document.createElement('table');
  for (var drug in data) {
    var row = document.createElement('tr');
    var tickercell = document.createElement('td');
    tickercell.innerHTML = drug;
    row.appendChild(tickercell);
    for (var i = 0; i < data[drug].length; i++){
      var cell = document.createElement('td');
      cell.innerHTML = data[drug][i];
      row.appendChild(cell);
    }
    table.appendChild(row);
  }
  var spot = document.querySelector('body');
  spot.appendChild(table);
}

function scrollingTicker(data){
  let output = ''
  for (var drug in data){
    output += drug + ' ' + data[drug][data[drug].length-1] + '  '
  }
  ticker = document.querySelector('.marquee');
  ticker.innerHTML = output;
}

window.addEventListener("load", function () {
    scrollingTicker(data);
    makeyTable(data);
});
