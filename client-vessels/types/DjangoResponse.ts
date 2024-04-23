import type Vessel from "./Vessel"

export interface DjangoResponse {
  count: number
  next: string | null
  previous: string | null
  results: Vessel[] | []
};
