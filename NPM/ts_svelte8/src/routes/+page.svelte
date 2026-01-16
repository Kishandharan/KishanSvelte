<script lang="ts"> 
    let output : number = 0;
    let inputElm : HTMLInputElement;

    function handle1(){
        let inputVal : number = Number(inputElm.value);
        for(let i = inputVal-1; i > 0; i--){
            inputVal = inputVal * i;
        }
        output = inputVal;
    }
</script>

<input type="number" bind:this={inputElm}>
<button onclick={handle1}>Get Factorial</button>
<p>{output}</p>

<style>
</style>