# Analysis Each Row

Each row of the log file is split by space like `uri used_time`, In this step, we need statistics each uri been requested times, then return the result in directory like:

```
{
    "/create/order": 199,
    "/query/order/info": 20,
    ...
}
```

## Tips

- Use the directory to store each uri requested times temporary.

## TODO

- Completing `uri_count.py`

## Requirements

- Finish the function `get_uri_and_count` and return the result.
