import type {PageLoad} from "./$types";

export const load : PageLoad = async ({params}) => {
  let name = params.name;
  let data = "Your name is "+name;
  return {"message":data};
};
