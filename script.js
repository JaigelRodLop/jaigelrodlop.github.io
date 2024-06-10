const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const chatLog = document.getElementById('chat-log');

chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const userInputValue = userInput.value.trim();
    if (userInputValue!== '') {
      fetch('http://localhost:5000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input: userInputValue })
      })
     .then(response => response.json())
     .then((data) => {
        if (data && data.response) {
          const responseText = data.response;
          chatLog.innerHTML += `<p>Usuario: ${userInputValue}</p><p>Bot: ${responseText}</p>`;
          userInput.value = '';
        } else {
          console.error('Error al procesar la respuesta del servidor');
        }
      })
     .catch((error) => {
        console.error(error);
      });
    }
  });