<p>This is the route2 page</p>
<script>
  let count = 0;
</script>

<p class="theme1">{count}</p>
<button on:click={()=>{count++}}>Increment</button>

<style>
  .theme1{
    font-size: 2rem;
  }
</style>
