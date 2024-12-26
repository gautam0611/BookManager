export default interface Job {
  id: string;
  company_name: string;
  title: string;
  location: string;
  salary: number;
  yoe: string;
  workLoc: string;
  dateApplied: Date;
  jobURL: string;
}

// interface ApiResponse {
//   [key: string]: Omit<Job, "id">;
// }