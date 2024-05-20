document.getElementById('submit').addEventListener('click', async function() {
    const a = parseFloat(document.getElementById('a').value);
    const b = parseFloat(document.getElementById('b').value);

    const addResult = await fetchResult('/add', { a, b });
    const subtractResult = await fetchResult('/subtract', { a, b });
    const multiplyResult = await fetchResult('/multiply', { a, b });
    const divideResult = await fetchResult('/divide', { a, b });

    document.getElementById('add-result').textContent = `Addition Result: ${addResult.result}`;
    document.getElementById('subtract-result').textContent = `Subtraction Result: ${subtractResult.result}`;
    document.getElementById('multiply-result').textContent = `Multiplication Result: ${multiplyResult.result}`;
    document.getElementById('divide-result').textContent = `Division Result: ${divideResult.result || divideResult.error}`;
});

async function fetchResult(endpoint, data) {
    const response = await fetch(`http://localhost:8001${endpoint}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    return response.json();
}
