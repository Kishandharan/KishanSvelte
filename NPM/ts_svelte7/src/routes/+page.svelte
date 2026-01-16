<script lang="ts">
    let joke : string = "Press the button first to get a joke"; 
    async function handle1(){
        let dat1 = await fetch("https://v2.jokeapi.dev/joke/Programming?type=single");    
        let dat2 = await dat1.json();
        let dat3 = dat2.joke;
        joke=dat3;
    }
</script>

<p class="joke">{joke}</p>
<button onclick={handle1}>Generate Joke</button>

<style>
</style>