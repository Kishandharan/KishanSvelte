import type {PageLoad} from "./$types";

export const load : PageLoad = async ({params}) => {
  let name1 = params.name;
  let mess1 = "Your name is "+name1;
  return {"message":mess1};
};
