<script>
  let jokes = $state([]);
  let numberOfJokes = $state(1);
  let apiUrlTemplate = `https://v2.jokeapi.dev/joke/Any?type=single&amount=${numberOfJokes}`;

  async function handle1(){
    if(numberOfJokes < 2){
      let data1 = await fetch(apiUrlTemplate);
      let data2 = await data1.json();
      let data3 = data2.joke;
      let uJokes = jokes;
      uJokes.push(data3);
      jokes = [];
      jokes = uJokes;
    }
  }
</script>

<h1>Jokes Generator</h1>
<input placeholder="Enter how many jokes you want" bind:value={numberOfJokes} type="number" />
<button onclick={handle1}>Fetch Jokes</button>
<ul>
  {#each jokes as joke}
    <li>{joke}</li>
  {/each}
</ul>

