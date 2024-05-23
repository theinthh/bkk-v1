function updateTime() {
  var now = new Date();
  var dateString = now.toLocaleDateString(undefined, {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
  var timeString = now.toLocaleTimeString(undefined, {
    hour: '2-digit',
    minute: '2-digit',
  });
  var dateTimeString = dateString + ' ' + timeString;
  document.getElementById('currenttime').innerHTML = dateTimeString;
};
setInterval(updateTime, 60000);
updateTime();