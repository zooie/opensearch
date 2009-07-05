
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

import org.sphx.api.SphinxClient;
import org.sphx.api.SphinxException;
import org.sphx.api.SphinxResult;
import org.sphx.api.SphinxMatch;

public class Search {
	public static void main (String[] argv) throws IOException, SphinxException {
		String index = "medindex";
		SphinxClient cl = new SphinxClient();

		cl.SetServer ("localhost", 8002);
		cl.SetWeights (new int[] {100, 1});
		cl.SetMatchMode (SphinxClient.SPH_MATCH_ANY);
		cl.SetLimits (0, 10);
		cl.SetSortMode (SphinxClient.SPH_SORT_RELEVANCE, "");

                Scanner scan = new Scanner(new File("../queries.txt"));
                String queryString;

                while (scan.hasNextLine()) {
                        queryString = scan.nextLine().trim();
		        SphinxResult res = cl.Query(queryString, index);

		        for (int i = 0; i < res.matches.length; i++) {
			        SphinxMatch info = res.matches[i];
			        System.out.println (queryString + " " + info.docId);
		        }
	        }
        }
}
