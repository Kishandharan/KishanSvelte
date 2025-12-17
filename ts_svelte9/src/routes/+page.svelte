<script lang="ts">
    let joke1 : string = "Press the button to get a joke.";

    async function handle1(){
        let url1 = "https://v2.jokeapi.dev/joke/Programming?type=single&amount=1";
        let dat1 = await fetch(url1);
        let dat2 = await dat1.json();
        let dat3 = dat2.joke;
        joke1 = dat3;
    }

</script>

<p>{joke1}</p>
<button onclick={handle1}>Get Joke</button>

<style>
</style>
