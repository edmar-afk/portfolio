// Function to reload the page after a delay
  function delayedReload() {
    // Set the delay in milliseconds (e.g., 3000ms = 3 seconds)
    const delay = 100;

    // Wait for the specified delay and then reload the page
    setTimeout(function() {
      location.reload();
    }, delay);
  }
