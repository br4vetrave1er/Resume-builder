console.log(document)
        
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
    var cookie = cookies[i].trim();
    // Does this cookie string begin with the name we want?
    if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
            }
        }
    }
return cookieValue;
}
function sendMessage() {
  var userInput = document.getElementById("user-input").value;
  console.log(userInput)
  var csrftoken = getCookie('csrftoken');
  var doc = sessionStorage.getItem('doc');
  var chatBody = document.getElementById('chat-messages');
  console.log(doc)
  // User message
  var userMessage = document.createElement('div');
  userMessage.classList.add('message', 'user-message');
  userMessage.innerHTML = '<p>' + userInput + '</p><div class="meta user">You<span>Just Now</span></div>';
  chatBody.appendChild(userMessage);

  var typingMessage = document.createElement('div');
typingMessage.classList.add('message', 'bot-message');
typingMessage.innerHTML = '<p>Bot is typing...</p><div class="meta bot">Bot<span>Just Now</span></div>';
chatBody.appendChild(typingMessage);


  if (userInput.trim() === '') return;
  else {
    fetch("http://127.0.0.1:8000/home/response/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'user-message': userInput,
        })
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log('data: ', data.result)
        
        chatBody.removeChild(typingMessage)
    
        // Bot response (just a simple example, replace with your bot logic)
        var botMessage = document.createElement('div');
        botMessage.classList.add('message', 'bot-message');
        botMessage.innerHTML = data.result;
        chatBody.appendChild(botMessage);
    })
    .catch(error => {
        console.log(error)
    })
  }

  

  // Scroll to the bottom
  chatBody.scrollTop = chatBody.scrollHeight;

  // Clear input field
  document.getElementById('user-input').value = '';
}

document.addEventListener('DOMContentLoaded', function() {
    var csrftoken = getCookie('csrftoken');
    var doc = sessionStorage.getItem('doc');
    console.log(doc)
    fetch("http://127.0.0.1:8000/home/bot-build/", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'data': doc,
        })
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        console.log(data)
        sessionStorage.setItem('bot', data.bot)
        console.log(data.bot)
    })
    .catch(error => {
        console.log(error)
    })
})

document.getElementById("message-form").addEventListener("submit", function(event) {
event.preventDefault(); // Prevent form submission
});

document.getElementById("user-input").addEventListener("keypress", function(event) {
if (event.key === "Enter") {
event.preventDefault(); // Prevent form submission
sendMessage(); // Call your sendMessage function
}
});

