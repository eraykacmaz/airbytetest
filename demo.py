# Import PyAirbyte
import airbyte as ab

# Show all available connectors
ab.get_available_connectors()

# Create and install the source:
source: ab.Source = ab.get_source("source-faker")

# Configure the source
source.set_config(
    config={
        "count": 50_000,  # Adjust this to get a larger or smaller dataset
        "seed": 123,
    },
)
# Verify the config and creds by running `check`:
source.check()
