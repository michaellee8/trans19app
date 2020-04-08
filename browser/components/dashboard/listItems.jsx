import React from "react";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";

import SupervisorAccountIcon from "@material-ui/icons/SupervisorAccount";

import Link from "../../src/Link";

export const mainListItems = (
  <div>
    <Link href={"/patients"}>
      <ListItem button>
        <ListItemIcon>
          <SupervisorAccountIcon />
        </ListItemIcon>
        <ListItemText primary="Patients" />
      </ListItem>
    </Link>
  </div>
);

export const secondaryListItems = (
  <div>
    {/*<ListSubheader inset>Saved reports</ListSubheader>*/}
    {/*<ListItem button>*/}
    {/*  <ListItemIcon>*/}
    {/*    <AssignmentIcon />*/}
    {/*  </ListItemIcon>*/}
    {/*  <ListItemText primary="Current month" />*/}
    {/*</ListItem>*/}
    {/*<ListItem button>*/}
    {/*  <ListItemIcon>*/}
    {/*    <AssignmentIcon />*/}
    {/*  </ListItemIcon>*/}
    {/*  <ListItemText primary="Last quarter" />*/}
    {/*</ListItem>*/}
    {/*<ListItem button>*/}
    {/*  <ListItemIcon>*/}
    {/*    <AssignmentIcon />*/}
    {/*  </ListItemIcon>*/}
    {/*  <ListItemText primary="Year-end sale" />*/}
    {/*</ListItem>*/}
  </div>
);
