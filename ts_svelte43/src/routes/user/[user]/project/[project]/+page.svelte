<script lang="ts">
  import {data} from "$lib/user_projects.ts";
  import {page} from "$app/state";

  let userName = page.params.user;
  let projectName = page.params.project;
</script>

{#if Object.keys(data).includes(userName)}
  {#if Object.keys(data[userName]).includes(projectName)}
    <p>{data[userName][projectName]}</p>
  {:else}
    <h1>Sorry, but we aren't able to find the project that you specified</h1>
  {/if}
{:else}
  <h1>Sorry, but we aren't able to find the user that you specified.</h1>
{/if}
