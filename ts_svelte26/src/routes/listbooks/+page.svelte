<script lang="ts">
  import {books} from "$lib/stores.ts";
  let bookNames:string[] = Object.keys($books);
</script>

<ul>
  {#each bookNames as bookName}
    <li>{bookName}</li>
  {/each}
</ul>

