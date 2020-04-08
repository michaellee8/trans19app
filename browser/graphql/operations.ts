/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: GetPatientDetail
// ====================================================

export interface GetPatientDetail_patient_histories_location_geometry {
  coordinates: any | null;
}

export interface GetPatientDetail_patient_histories_location {
  address: string;
  district: string;
  name: string;
  id: string;
  geometry: GetPatientDetail_patient_histories_location_geometry;
}

export interface GetPatientDetail_patient_histories {
  id: string;
  start: any;
  end: any;
  category: string;
  detail: string;
  location: GetPatientDetail_patient_histories_location | null;
}

export interface GetPatientDetail_patient {
  id: string; // The ID of the object.
  name: string;
  hkid: string;
  birthday: any;
  confirmedDay: any;
  caseNum: number;
  histories: GetPatientDetail_patient_histories[];
}

export interface GetPatientDetail {
  patient: GetPatientDetail_patient | null; // The ID of the object
}

export interface GetPatientDetailVariables {
  id: string;
}

/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: Patients
// ====================================================

export interface Patients_allPatients_edges_node {
  id: string; // The ID of the object.
  name: string;
  hkid: string;
  confirmedDay: any;
  caseNum: number;
}

export interface Patients_allPatients_edges {
  node: Patients_allPatients_edges_node | null; // The item at the end of the edge
}

export interface Patients_allPatients_pageInfo {
  hasNextPage: boolean; // When paginating forwards, are there more items?
  hasPreviousPage: boolean; // When paginating backwards, are there more items?
  startCursor: string | null; // When paginating backwards, the cursor to continue.
  endCursor: string | null; // When paginating forwards, the cursor to continue.
}

export interface Patients_allPatients {
  edges: (Patients_allPatients_edges | null)[]; // Contains the nodes in this connection.
  pageInfo: Patients_allPatients_pageInfo; // Pagination data for this connection.
}

export interface Patients {
  allPatients: Patients_allPatients | null;
}

export interface PatientsVariables {
  cursor?: string | null;
}

/* tslint:disable */
// This file was automatically generated and should not be edited.

//==============================================================
// START Enums and Input Objects
//==============================================================

//==============================================================
// END Enums and Input Objects
//==============================================================
