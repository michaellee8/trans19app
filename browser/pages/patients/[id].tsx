import React from "react";
import Layout from "../../components/Layout";
import PatientsList from "../../components/PatientsList";
import PatientDetail from "../../components/PatientDetail";
import { withApollo } from "../../lib/apollo";

const PatientDetailPage = () => (
  <Layout title={"Patient Detail"}>
    <div>
      <PatientDetail />
    </div>
  </Layout>
);

export default withApollo({ ssr: true })(PatientDetailPage);
