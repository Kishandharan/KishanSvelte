<script>
    let input;    
    let output = 0;

    function handle1(){
        let fact = Number(input.value);        
        for(let i = fact-1; i >= 1; i--){
            fact = fact * i;
        }
        output = fact;
    }
</script>

<h1>Factorial Calculator</h1>
<input bind:this={input} />
<button on:click={handle1}>Get Factorial</button>
<p>{output}</p>

<style>
    h1{
        text-decoration: underline;
    }
</style>
