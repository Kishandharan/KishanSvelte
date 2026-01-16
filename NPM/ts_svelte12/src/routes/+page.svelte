<script lang="ts">
    import "../app.css";
    let output : string;
    async function handle1(){
        let data1 = await fetch("https://v2.jokeapi.dev/joke/Programming?type=single");
        let data2 = await data1.json();
        let data3 = data2.joke;
        output = data3;
    }
</script>

<p>{output}</p>
<button onclick={handle1}>Get joke</button>

<style></style>