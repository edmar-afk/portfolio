const searchInput = document.getElementById('searchInput');
		const itemsContainer = document.getElementById('itemsContainer');
		const items = itemsContainer.getElementsByClassName('box');
		const noMatchText = document.getElementById('noMatchText');

		searchInput.addEventListener('input', function () {
			const query = searchInput.value.toLowerCase();
			let matchFound = false;

			for (let i = 0; i < items.length; i++) {
				const item = items[i];
				const text = item.innerText.toLowerCase();

				if (text.includes(query)) {
					item.style.display = 'block';
					matchFound = true;
				} else {
					item.style.display = 'none';
				}
			}

			// Show the "No matching items found" text if no match is found
			if (!matchFound) {
				noMatchText.style.display = 'block';
			} else {
				noMatchText.style.display = 'none';
			}
		});