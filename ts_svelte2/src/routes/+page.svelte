<script lang="ts">
    let color = "red";
    function handle1(){
        if(color == "red"){
            color = "blue";
        }else{
            color = "red";
        }
    }
</script>

<h1>Color Toggler</h1>
<button on:click={handle1}>Toggle Colors</button>
<div class="colordiv" style:background-color={color}></div>

<style>
    .colordiv{
        width: 100px;
        height: 100px;
        transition: 1s ease;
    }
</style>
