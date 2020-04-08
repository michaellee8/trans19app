

/* tslint:disable */
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL query operation: Pateients
// ====================================================

export interface Pateients_allPatients_edges_node {
  id: string;  // The ID of the object.
  name: string;
  hkid: string;
  confirmedDay: any;
  caseNum: number;
}

export interface Pateients_allPatients_edges {
  node: Pateients_allPatients_edges_node | null;  // The item at the end of the edge
}

export interface Pateients_allPatients_pageInfo {
  hasNextPage: boolean;        // When paginating forwards, are there more items?
  hasPreviousPage: boolean;    // When paginating backwards, are there more items?
  startCursor: string | null;  // When paginating backwards, the cursor to continue.
  endCursor: string | null;    // When paginating forwards, the cursor to continue.
}

export interface Pateients_allPatients {
  edges: (Pateients_allPatients_edges | null)[];  // Contains the nodes in this connection.
  pageInfo: Pateients_allPatients_pageInfo;       // Pagination data for this connection.
}

export interface Pateients {
  allPatients: Pateients_allPatients | null;
}

export interface PateientsVariables {
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