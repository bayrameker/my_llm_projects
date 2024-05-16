async function generateCode() {
    const prompt = document.getElementById('prompt').value;
    try {
        const response = await fetch('http://localhost:5000/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt })
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const result = await response.json();
        document.getElementById('result').textContent = result.generated_text;
    } catch (error) {
        console.error('There has been a problem with your fetch operation:', error);
    }
}
