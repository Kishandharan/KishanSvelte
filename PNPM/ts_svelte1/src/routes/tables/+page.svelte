<script lang="ts">
  let start1:number = $state(); // Table Starting
  let end1:number = $state(); // Table Ending
  let start2:number = $state(); // Multiplier Starting 
  let end2:number = $state(); // Multiplier Ending
  let tables:string[][] = $state([]);

  function handle1(){
    let index1 = 0; // Table Index
    for(let j = Number(start1); j <= Number(end1); j++){
      tables.push([]);
      for(let i = Number(start2); i <= Number(end2); j++){
        tables[index1].push(`${i}*${j}=${i*j}`);
      }
      index1++;
    }
    console.log(tables);
  }
</script>

<input bind:value={start1} type="number" placeholder="Enter table starting"><br>
<input bind:value={end1} type="number" placeholder="Enter table ending"><br>
<input bind:value={start2} type="number" placeholder="Enter multiplier starting"><br>
<input bind:value={end2} type="number" placeholder="Enter multiplier ending"><br>
<button onclick={handle1}> Generate Tables </button>
