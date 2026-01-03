<script lang="ts">
  import {books} from "$lib/stores.ts";
  let newBookName:string = $state();
  let newBookDesc:string = $state();
  let newBookCont:string = $state();

  function handle1(){
    $books = {...$books, `${newBookName}`:[newBookDesc, newBookCont]};
    alert("Created Book Successfully!");
    console.log($books);
  }
    
</script>

<div class="margintop">
  <input bind:this={newBookName} type="text" placeholder="Enter new book name"/><br>
  <textarea bind:this={newBookDesc} placeholder="Enter new book Description" /><br>
  <textarea bind:this={newBookCont} placeholder="Enter new book Content" /><br>
  <button onclick={handle1}>Create Book</button>
</div>

<style>
  .margintop{
    margin-top: 10px;
  }
</style>


