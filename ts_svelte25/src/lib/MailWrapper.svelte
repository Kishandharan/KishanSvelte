<script lang="ts">
  import type {Snippet} from "svelte";
  interface propsType{
    inName: string;
    ouName: string;
    children: Snippet;
  }

  let {inName, ouName, children}:propsType = $props();
</script>

<p>Dear {ouName},</p><br>
{@render children()}
<br>
<p>Thanks and Regards - {inName}</p>

