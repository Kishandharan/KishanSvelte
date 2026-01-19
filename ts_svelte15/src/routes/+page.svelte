<script>
   let url1 = "http://172.105.253.146/viewholidays/";
   let output;
   async function handle1(){
     let data1 = await fetch(url1);
     let data2 = await data1.json();
     let data3 = data2.response;
     output = data3;
     console.log(output);
   }
</script>

<button on:click={handle1}>Fetch</button>

<ul>
  {#each output as item}
    <li>{item[1]+" - "+item[2]}</li>
  {/each}
</ul>

<style>
  button{
    background-color: #4970f2;
    border: none;
    color: white;
    padding: 4px;
    border-radius: 7px;
    font-size: 2rem;
  }

  li{
    font-size: 2rem;
  }
</style>
