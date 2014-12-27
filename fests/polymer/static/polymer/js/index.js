document.addEventListener('polymer-ready', function() {
  var navicon = document.getElementById('navicon');
  var drawerPanel = document.getElementById('drawer-panel');
  navicon.addEventListener('click', function() {
    drawerPanel.togglePanel();
  });

  var tabs = document.querySelector('paper-tabs');

  tabs.addEventListener('core-select', function() {
    console.log("Selected: " + tabs.selected);
  });
});

