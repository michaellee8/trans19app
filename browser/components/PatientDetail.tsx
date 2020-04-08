import { gql } from "apollo-boost";
import Router, { useRouter } from "next/router";
import { useQuery } from "@apollo/react-hooks";
import {
  GetPatientDetail,
  GetPatientDetailVariables,
  Patients,
  PatientsVariables,
} from "../graphql/operations";
import { Grid, TableRow } from "@material-ui/core";
import { spacing } from "@material-ui/system";
import React from "react";
import Paper from "@material-ui/core/Paper";
import { makeStyles } from "@material-ui/styles";
import Table from "@material-ui/core/Table";
import TableHead from "@material-ui/core/TableHead";
import TableCell from "@material-ui/core/TableCell";
import TableBody from "@material-ui/core/TableBody";

const GET_PATIENT_DETAIL = gql`
  query GetPatientDetail($id: ID!) {
    patient(id: $id) {
      id
      name
      hkid
      birthday
      confirmedDay
      caseNum
      histories {
        id
        start
        end
        category
        detail
        location {
          address
          district
          name
          id
          geometry {
            coordinates
          }
        }
      }
    }
  }
`;

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    height: 140,
    width: 100,
  },
  control: {
    padding: 0,
  },
}));

const PatientDetail = () => {
  const router = useRouter();
  // @ts-ignore
  const { id }: { id: string } = router.query;
  const { data, loading, fetchMore } = useQuery<
    GetPatientDetail,
    GetPatientDetailVariables
  >(GET_PATIENT_DETAIL, { variables: { id } });
  const patient = data?.patient;
  const classes = useStyles();

  if (loading || !data || !data.patient) {
    return <p>Loading...</p>;
  }

  return (
    <Grid container className={classes.root} spacing={2}>
      <Grid item xs={12}>
        <Grid container justify="center" spacing={2}>
          <Grid item>
            <p>Name: {patient?.name}</p>
            <p>HKID: {patient?.hkid}</p>
            <p>Birthday: {patient?.birthday}</p>
            <p>Confirmed Day: {patient?.confirmedDay}</p>
            <p>Case Number: {patient?.caseNum}</p>
          </Grid>
          <Grid item>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>Start</TableCell>
                  <TableCell>End</TableCell>
                  <TableCell>Category</TableCell>
                  <TableCell>Name</TableCell>
                  <TableCell>District</TableCell>
                  <TableCell>Address</TableCell>
                  <TableCell>Detail</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {patient?.histories?.map((history) => (
                  <TableRow key={history.id}>
                    <TableCell>{history.start}</TableCell>
                    <TableCell>{history.end}</TableCell>
                    <TableCell>{history.category}</TableCell>
                    <TableCell>{history.location?.name}</TableCell>
                    <TableCell>{history.location?.district}</TableCell>
                    <TableCell>{history.location?.address}</TableCell>
                    <TableCell>{history.detail}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default PatientDetail;
