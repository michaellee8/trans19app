import { GetStaticProps } from "next";
import Link from "next/link";

import { User } from "../../interfaces";
import { sampleUserData } from "../../utils/sample-data";
import Layout from "../../components/Layout";
import List from "../../components/List";
import { gql } from "apollo-boost";
import { withApollo } from "../../lib/apollo";
import PatientsList from "../../components/PatientsList";
import React from "react";

const PatientsIndexPage = () => (
  <Layout title={"Patients"}>
    <div>
      <PatientsList />
    </div>
  </Layout>
);

export default withApollo({ ssr: true })(PatientsIndexPage);
