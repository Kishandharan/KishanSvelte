<script lang="ts">
  import {data} from "$lib/user_projects.ts";
  import {page} from "$app/state";

  let userName = page.params.user;
</script>

{#if Object.keys(data).includes(userName)}
  <ul>
    {#each Object.keys(data[userName]) as project}
      <li><a href={`/user/${userName}/project/${project}`}>{project}</a></li>
    {/each}
  </ul>
{:else}
  <h1>Sorry, but we cannot find that user...😕😕</h1>
{/if}
