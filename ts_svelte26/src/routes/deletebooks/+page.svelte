<script lang="ts">
  import {books} from "$lib/stores.ts";
  let bookName:string = $state();
  function handle1(){
    delete $books[bookName];
    console.log($books);
    alert("Deleted Book Successfully");
  }
</script>

<div class="margintop">
  <input bind:value={bookName} type="text" placeholder="Enter book name">
  <button onclick={handle1}>Delete Book</button>
</div>

