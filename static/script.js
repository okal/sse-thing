var eventSource = new EventSource("remote");

eventSource.addEventListener("ping", function(e) { console.log(e.data)}, false)

eventSource.onmessage = function(e) {
    console.log(e);
}
eventSource.onerror = function(e) {
    console.log(e);
}