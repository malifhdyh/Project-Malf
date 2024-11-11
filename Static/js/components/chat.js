document.addEventListener('DOMContentLoaded', function() {
    const chatIcon = document.getElementById('chatIcon');
    const chatWindow = document.getElementById('chatWindow');
    const closeChat = document.getElementById('closeChat');
    const messageInput = document.getElementById('messageInput');
    const sendMessage = document.getElementById('sendMessage');
    const chatMessages = document.getElementById('chatMessages');
    
    // Toggle chat window
    chatIcon.addEventListener('click', () => {
        chatWindow.classList.toggle('active');
        // Remove notification badge when chat is opened
        const badge = chatIcon.querySelector('.notification-badge');
        if (badge) badge.style.display = 'none';
    });
    
    closeChat.addEventListener('click', () => {
        chatWindow.classList.remove('active');
    });
    
    // Send message function
    function sendUserMessage() {
        const message = messageInput.value.trim();
        if (message) {
            // Add user message
            addMessage(message, 'user');
            messageInput.value = '';
            
            // Simulate agent response
            setTimeout(() => {
                const responses = [
                    "Thanks for your message! I'll help you with that.",
                    "Let me check that for you.",
                    "I understand what you're looking for.",
                    "I'm here to help! Could you provide more details?"
                ];
                const randomResponse = responses[Math.floor(Math.random() * responses.length)];
                addMessage(randomResponse, 'agent');
            }, 1000);
        }
    }
    
    // Add message to chat
    function addMessage(content, type) {
        const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        const messageHTML = `
            <div class="message ${type}">
                <div class="message-content">${content}</div>
                <div class="message-time">${time}</div>
            </div>
        `;
        chatMessages.insertAdjacentHTML('beforeend', messageHTML);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    // Send message events
    sendMessage.addEventListener('click', sendUserMessage);
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendUserMessage();
        }
    });
    
    // Auto-resize textarea
    messageInput.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = (this.scrollHeight) + 'px';
    });
});