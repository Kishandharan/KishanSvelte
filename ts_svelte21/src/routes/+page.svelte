<script lang="ts">
  let number = $state(1);
  $effect(()=>{
    console.log(number);
  })
</script>

<button on:click={()=>{number=3}}>Set number to 3</button>

