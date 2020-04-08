import { gql } from "apollo-boost";
import Router, { useRouter } from "next/router";
import { useQuery } from "@apollo/react-hooks";
import {
  GetPatientDetail,
  GetPatientDetailVariables,
  Patients,
  PatientsVariables,
} from "../graphql/operations";
import { Grid } from "@material-ui/core";
import { spacing } from "@material-ui/system";
import React from "react";
import Paper from "@material-ui/core/Paper";
import { makeStyles } from "@material-ui/styles";

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
          <Grid>
            <p>Name: {patient?.name}</p>
            <p>HKID: {patient?.hkid}</p>
            <p>Birthday: {patient?.birthday}</p>
            <p>Confirmed Day: {patient?.confirmedDay}</p>
            <p>Case Number: {patient?.caseNum}</p>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  );
};

export default PatientDetail;
