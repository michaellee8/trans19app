import { gql } from "apollo-boost";
import { TableContainer, Paper, Table } from "@material-ui/core";
import { makeStyles } from "@material-ui/styles";
import TableRow from "@material-ui/core/TableRow";
import TableHead from "@material-ui/core/TableHead";
import TableCell from "@material-ui/core/TableCell";
import { useQuery } from "@apollo/react-hooks";
import { Patients, PatientsVariables } from "../graphql/operations";
import TableBody from "@material-ui/core/TableBody";
import Router from "next/router";
import React from "react";

const ALL_PATIENTS_QUERY = gql`
  query Patients($cursor: String) {
    allPatients(first: 10, after: $cursor) {
      edges {
        node {
          id
          name
          hkid
          confirmedDay
          caseNum
        }
      }
      pageInfo {
        hasNextPage
        hasPreviousPage
        startCursor
        endCursor
      }
    }
  }
`;

const useStyles = makeStyles({
  table: {
    // maxWidth: 400,
  },
});

const PatientsList = () => {
  const classes = useStyles();

  const { data, loading, fetchMore } = useQuery<Patients, PatientsVariables>(
    ALL_PATIENTS_QUERY
  );

  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <TableContainer component={Paper}>
      <Table className={classes.table} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Case Number</TableCell>
            <TableCell>Name</TableCell>
            <TableCell>HKID</TableCell>
            <TableCell>Confirmed Day</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data &&
            data.allPatients?.edges?.map(
              (edge) =>
                edge &&
                edge.node && (
                  <TableRow
                    key={edge.node.id}
                    onClick={() => Router.push(`/patients/${edge?.node?.id}`)}
                  >
                    <TableCell>{edge.node.caseNum}</TableCell>
                    <TableCell>{edge.node.name}</TableCell>
                    <TableCell>{edge.node.hkid}</TableCell>
                    <TableCell>{edge.node.confirmedDay}</TableCell>
                  </TableRow>
                )
            )}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default PatientsList;
