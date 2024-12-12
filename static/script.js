document.getElementById('search-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const searchInput = document.getElementById('search-input');
    const resultsDiv = document.getElementById('results');
   
    // Create loading spinner
    resultsDiv.innerHTML = `
        <div class="loading-spinner">
            <div class="spinner"></div>
            <p>Searching...</p>
        </div>
    `;

    try {
        const formData = new FormData();
        formData.append('search', searchInput.value);
        const response = await fetch('http://localhost:5000/search', {
            method: 'POST',
            body: formData
        });
        const products = await response.json();
        // Display results
        console.log(products)
        resultsDiv.innerHTML = products.map(product =>
        {
            switch(product.website.toLowerCase())
            {
                case 'amaflip':
                    return `
                        <div class="product-card">
                        <img src="${product.image_url}" alt="${product.name}">
                        <a class = "imgthingy" href = "${product.prd_link}">
                        <span>${product.name}</span>
                        </a>
                        <p>Price: ${product.price}</p>
                        <p>Rating: ${product.rating}</p>
                        </div>`;
                
                case 'zekit':
                    return `
                        <div class="product-card">
                        <img src="${product.image_url}" alt="${product.name}">
                        <a class = "imgthingy" href = "${product.prd_link}">
                        <span>${product.name}</span>
                        </a>
                        <p>Price: ${product.price}</p>
                        <p>Weight: ${product.rating}</p>
                        </div>`;
            }
        }
    ).join('');
    } catch (error) {
        resultsDiv.innerHTML = `Error: ${error.message}`;
    }
});