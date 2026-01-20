<script lang="ts">
  import {data} from "$lib/users_projects.ts";
  import {page} from "$app/state";

  let userName = page.params.user;
</script>

{#if Object.keys(data).includes(userName)}
  <ul>
    {#each data[userName] as project}
      <li>{project}</li>    
    {/each}
  </ul>
{:else}
  <h1>User Not Found..</h1>
{/if}
