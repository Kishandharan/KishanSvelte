<script lang="ts">
  import {books} from "$lib/stores.ts";

  let bookName:string = $state();
  let bookDesc:string = $state();
  let bookCont:string = $state();
  
  function handle1(){
    bookDesc.innerText = `Book Description: ${$books[bookName][0]}`;
    bookCont.innerText = `Book's Content: ${$books[bookName][1]}
    `;
  }

</script>

<div class="margintop">
  <input type="text" placeholder="Enter Book Name" bind:value={bookName}/>
  <button onclick={handle1}>Inspect Book</button>
  <p bind:this={bookDesc}></p>
  <p bind:this={bookCont}></p>
</div>

