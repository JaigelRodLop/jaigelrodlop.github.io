const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const chatLog = document.getElementById('chat-log');

chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const userInputValue = userInput.value.trim();
    if (userInputValue !== '') {
      fetch('/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input: userInputValue })
      })
      .then(response => response.json())
      .then((data) => {
        const responseText = data.response;
        chatLog.innerHTML += `<p>Usuario: ${userInputValue}</p><p>Bot: ${responseText}</p>`;
        userInput.value = '';
      })
      .catch((error) => {
        console.error(error);
      });
    }
  });