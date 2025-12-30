<script>
  let prom1 = new Promise(function(resolve, reject){
    setTimeout(()=>{
    resolve("Resolved!");
    }, 1000);
  });
</script>

{#await prom1}
  <p>Loading...</p>
{:then value}
  <p>{value}</p>
{/await}

<style>
  /* your styles go here */
</style>
