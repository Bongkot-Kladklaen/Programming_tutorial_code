const seartch_term = document.getElementById('search_q');
const seartch_btn = document.getElementById('search-btn');

const getPokemonData = async query => {
    const url = `https://pokeapi.co/api/v2/pokemon/${query}`
    const response = await fetch(url)

    if(response.status == 404 || response.statusText == 'Not Found'){
        document.getElementById('show_error').classList.add('show')
        document.getElementById('show_error').classList.remove('hidden')
        return
    }
    
    const pokemon = await response.json()
    
    if(response.status == 200){
        document.getElementById('show_error').classList.remove('show')
    }

    let types_secound=''
    if(pokemon.types[1]){
        types_secound = ` / ${pokemon.types[1].type.name}`
    }

    document.getElementById('update_img').setAttribute('src',pokemon.sprites.other.dream_world.front_default)
    document.getElementById('update_name').innerHTML = pokemon.name
    document.getElementById('update_hp').innerHTML = `HP ${Math.floor(Math.floor() * pokemon.stats[0].base_stat) + 1}`
    document.getElementById('update_xp').innerHTML = `XP ${pokemon.base_experience}`
    document.getElementById('update_type').innerHTML = `${pokemon.types[0].type.name}${types_secound}`
    document.getElementById('update_weight').innerHTML = `${pokemon.weight}kg`
    document.getElementById('update_height').innerHTML = `${pokemon.height}m`
    document.getElementById('update_stardust').innerHTML = Math.floor((Math.floor() * 10000) + 1 )
    document.getElementById('update_candy').innerHTML = Math.floor((Math.floor() * 500) + 1 )
    document.getElementById('update_candy_title').innerHTML = `${pokemon.name} Candy`
  
}

seartch_btn.addEventListener('click',() => getPokemonData(seartch_term.value))