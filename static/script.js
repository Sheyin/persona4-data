// This helps with search by suggesting a name as you type
function suggestSearchResults(event) {

	const list_of_persona_names = ['Izanagi', 'Yomotsu-Shikome', 'Obariyon', 'Legion', 'Ose', 'Black Frost', 'Decarabia', 'Shiki-Ouji', 'Loki', 'Pixie', 'Orobas', 'Jack Frost', 'Hua Po', 'Pyro Jack', 'Dis', 'Rangda', 'Jinn', 'Surt', 'Mada', 'Saki Mitama', 'Sarasvati', 'High Pixie', 'Ganga', 'Parvati', 'Kikuri-Hime', 'Hariti', 'Tzitzimitl', 'Scathach', 'Senri', 'Yaksini', 'Titania', 'Gorgon', 'Gabriel', 'Skadi', 'Mother Harlot', 'Alilat', 'Isis', 'Oberon', 'King Frost', 'Setanta', 'Oukuninushi', 'Thoth', 'Pabilsag', 'Barong', 'Odin', 'Omoikane', 'Anzu', 'Shiisaa', 'Unicorn', 'Flauros', 'Hokuto Seikun', 'Cerberus', 'Daisoujou', 'Hachiman', 'Kohryu', 'Queen Mab', 'Undine', 'Leanan Sidhe', 'Raphael', 'Cybele', 'Ishtar', 'Slime', 'Nata Taishi', 'Eligor', 'Ara Mitama', 'Ares', 'Triglav', 'Kin-ki', 'Thor', 'Atavaka', 'Futsunushi', 'Angel', 'Archangel', 'Principality', 'Power', 'Virtue', 'Dominion', 'Throne', 'Uriel', 'Melchizedek', 'Sraosha', 'Forneus', 'Ippon-Datara', 'Lamia', 'Mothman', 'Hitokoto-Nushi', 'Kurama Tengu', 'Niddhoggr', 'Nebiros', 'Arahabaki', 'Ongyo-ki', 'Fortuna', 'Clotho', 'Lachesis', 'Ananta', 'Atropos', 'Norn', 'Sandman', 'Valkyrie', 'Titan', 'Rakshasa', 'Kusi Mitama', 
	'Oni', 'Hanuman', 'Kali', 'Siegfried', 'Zaou-Gongen', 'Berith', 'Yomotsu-Ikusa', 'Makami', 'Orthrus', 'Yatsufusa', 'Taowu', 'Hell Biker', 'Vasuki', 'Attis', 'Ghoul', 'Mokoi', 'Matador', 'Samael', 'Mot', 'White Rider', 'Alice', 'Mahakala', 'Apsaras', 'Sylph', 'Xiezhai', 'Nigi Mitama', 'Mithra', 'Genbu', 'Seiryu', 'Suzaku', 'Byakko', 'Yurlungur', 'Vishnu', 'Ukobach', 'Lilim', 'Vetala', 'Incubus', 'Pazuzu', 'Succubus', 'Lilith', 'Belphegor', 'Belial', 'Beelzebub', 'Taotie', 'Cu Chulainn', 'Abaddon', 'Mara', 'Masakado', 'Yoshitsune', 'Shiva', 'Kaiwan', 'Neko Shogun', 'Fuu-ki', 'Ganesha', 'Garuda', 'Kartikeya', 'Saturnus', 'Helel', 'Andra', 'Nozuchi', 'Yamata-no-Orochi', 'Alraune', 'Girimehkala', 'Sui-ki', 'Seth', 'Baal Zebul', 'Sandalphon', 'Cu Sith', 'Phoenix', 'Gdon', 'Yatagarasu', 'Narasimha', 'Tam Lin', 'Jatayu', 'Horus', 'Suparna', 'Asura', 'Anubis', 'Trumpeter', 'Michael', 'Satan', 'Metatron', 'Ardha', 'Lucifer', 'Gurr', 'Take-Minakata', 'Pale Rider', 'Loa', 'Baphomet', 'Kumbhanda', 'Chernobog', 'Seiten Taisei', 'Magatsu Izanagi', 'Ame-no-Uzume', 'Narcissus', 'Sati', 'Raja Naga', 'Kushinada-Hime', 'Quetzalcoatl', 'Kingu', 'Lakshmi', 'Kaguya', 'Izanagi-no-Okami'].sort();

	const text = event.value;
	console.log(event.value);
	// Get first character of entered text, get second character, etc
	let re = new RegExp('^' + text);
	let results = [];

	list_of_persona_names.forEach(name => {
		if (re.test(name.toLowerCase())) {
			results.push(name);
		}
	})
	console.log(results);
	showSuggestedNames(results);
	return;
}



// Expects an array of strings(names).
// Adds them to the (hidden) #search-results div.
function showSuggestedNames(names) {
	const searchResultsBox = document.getElementById('search-results');
	searchResultsBox.innerHTML = "";

	//searchResultsBox.innerHTML="Do you mean... </ br>";
	names.forEach(name => {
		//searchResultsBox.innerHTML += '<div class="search-suggestion">' + name + '</div>';
		// The above line works, but trying this the proper(?) way
		const newNode = document.createElement("div");
		newNode.className = "search-suggestion";
		const text = document.createTextNode(name);
		newNode.addEventListener('click', searchThisName);
		newNode.appendChild(text);
		searchResultsBox.append(newNode);
	})
	return;
}

const searchThisName = (event) => {
	console.log(event.target.lastChild.textContent);
	const selectedName = event.target.lastChild.textContent;
	const inputBox = document.getElementById('persona');
	inputBox.value = selectedName;
	document.getElementById('persona-search').submit();
	return;
}